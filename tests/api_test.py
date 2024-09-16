from discoauth import auth, discord

# if it doesn't make sense, check the workflow for testing. The workflow adds variables, to keep the environment variables secret

async def test_make_api():
    api = discord(clid, clsec, ["identify"], "https://www.example.com")
    token = await api.token(code)

async def test_get_user():
    api = discord(clid, clsec, ["identify"], "https://www.example.com")
    token = await api.token(code)
    user1 = await api.user(token).fetch(clid)
    user2 = await api.user(token).fetch()

