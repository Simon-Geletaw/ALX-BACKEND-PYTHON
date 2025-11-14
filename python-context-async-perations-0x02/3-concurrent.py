import asyncio
import aiosqlite

async def async_fetch_users():
    async with connection.execute("SELECT * FROM users") as cursor:
        print("start executing users")
        results = await cursor.fetchall()
        return results

async def async_fetch_older_users():
    async with connection.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
        print("executing the age part")
        results_age = await cursor.fetchall()
        return results_age

async def fetch_concurrently():
    async with aiosqlite.connect('users.db') as conn:
        
        # Create tasks
        task1 = asyncio.create_task(async_fetch_users(conn))
        task2 = asyncio.create_task(async_fetch_older_users(conn))

        # Run tasks concurrently
        results = await asyncio.gather(task1, task2)

        # Print results
        print("All users:", results[0])
        print("Older users:", results[1])

asyncio.run(fetch_concurrently())
