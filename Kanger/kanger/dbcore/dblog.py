from Kanger.kanger.dbcore import mongo_client

logsdb = mongo_client["Kanger"]["logs"]
statuslogdb = mongo_client["Kanger"]["statuslog"]

async def start_botlog(user_id: int):
    user_data = await statuslogdb.users.find_one({"user_id": user_id})
    if user_data:
        await statuslogdb.users.update_one(
            {"user_id": user_id},
            {"$set": {"status_log": True}},
        )
    else:
        await statuslogdb.users.insert_one(
            {"user_id": user_id, "status_log": True}
        )

async def stop_botlog(user_id: int):
    await statuslogdb.users.delete_one({"user_id": user_id, "status_log": True})

async def status_botlog(user_id: int):
    user_data = await statuslogdb.users.find_one({"user_id": user_id, "status_log": True})
    return user_data

async def get_botlog(user_id: int):
    user_data = await logsdb.users.find_one({"user_id": user_id, "botlog_chat_id": botlog_chat_id})
    return user_data
    
async def set_botlog(user_id: int, botlog_chat_id: int):
    user_data = await logsdb.users.find_one({"user_id": user_id})
    if user_data:
        await logsdb.users.update_one(
            {"user_id": user_id},
            {"$set": {"botlog_chat_id": botlog_chat_id}},
        )
    else:
        await logsdb.users.insert_one(
            {"user_id": user_id, "botlog_chat_id": botlog_chat_id}
        )

async def delete_botlog(user_id: int):
    await logsdb.users.delete_one({"user_id": user_id})