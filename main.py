import sys
import traceback
from fastapi import FastAPI, Request, Response
from botbuilder.core import (
    BotFrameworkAdapterSettings, 
    BotFrameworkAdapter, 
    TurnContext
)
from botbuilder.schema import Activity
from src.agent_logic import create_mining_agent
from src.config import os
from src.config import MS_APP_ID, MS_APP_PASSWORD, MS_APP_TYPE, MS_TENANT_ID

app = FastAPI()

# 1. Adapter Settings
SETTINGS = BotFrameworkAdapterSettings(
    app_id=MS_APP_ID,
    app_password=MS_APP_PASSWORD,
    channel_auth_tenant=MS_TENANT_ID # Use 'common' for multi-tenant
)
ADAPTER = BotFrameworkAdapter(SETTINGS)

# 2. Instantiate the Agent
agent_executor = create_mining_agent()

async def on_message_activity(turn_context: TurnContext):
    user_input = turn_context.activity.text
    try:
        # 3. Invoke LangChain SQL Agent
        response = agent_executor.invoke({"input": user_input})
        await turn_context.send_activity(response["output"])
    except Exception as e:
        await turn_context.send_activity(f"Error: {str(e)}")

@app.post("/api/messages")
async def messages(request: Request):
    # 4. Handle the Teams Webhook
    body = await request.json()
    activity = Activity().from_dict(body)
    auth_header = request.headers.get("Authorization", "")

    async def aux_func(turn_context):
        if activity.type == "message":
            await on_message_activity(turn_context)

    try:
        await ADAPTER.process_activity(activity, auth_header, aux_func)
        return Response(status_code=201)
    except Exception as e:
        print(traceback.format_exc())
        return Response(status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3978)