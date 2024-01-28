import asyncio
from pytgcalls import GroupCallFactory
from PyroUbot import *

class Client:
    def invoke(self):
        print("Invoke method")

async def start_ubot(user_id, _ubot):
    ubot_ = Ubot(**_ubot)
    try:
        await asyncio.wait_for(ubot_.start(), timeout=30)
        
        if hasattr(ubot_, 'invoke') and callable(getattr(ubot_, 'invoke', None)):
            setattr(ubot_, 'send', getattr(ubot_, 'invoke'))
        else:
            print(f"Error: 'invoke' method is not available for {ubot_}")

    except asyncio.TimeoutError:
        await remove_ubot(user_id)
        await add_prem(user_id)
        await sending_user(user_id)
        print(f"[𝗜𝗡𝗙𝗢] - ({user_id}) 𝗧𝗜𝗗𝗔𝗞 𝗗𝗔𝗣𝗔𝗧 𝗠𝗘𝗥𝗘𝗦𝗣𝗢𝗡")
    except Exception as e:
        await remove_ubot(user_id)
        await rm_all(user_id)
        await rem_expired_date(user_id)
        for X in await get_chat(user_id):
            await remove_chat(user_id, X)
        print(f"✅ {user_id} 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 𝗗𝗜𝗛𝗔𝗣𝗨𝗦 - {e}")

async def main():
    tasks = []
    for _ubot in await get_userbots():
        tasks.append(asyncio.create_task(start_ubot(int(_ubot["name"]), _ubot)))
        if not hasattr(_ubot, "group_call"):
            _ubot["group_call"] = GroupCallFactory(_ubot).get_group_call()

    try:
        await asyncio.gather(*tasks, bot.start())
        await asyncio.gather(loadPlugins(), installPeer(), expiredUserbots(), idle())
    except Exception as main_error:
        print(f"Main error: {main_error}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
