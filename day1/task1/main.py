import asyncio
from json import loads, dumps;
from service import get_user;
from utils import print_user, to_json, devide;




user = get_user(1);
print_user(user);
to_json(user);''


def run_division(a, b):
    try:
        result = devide(a, b);
        print(f"Result: {result}");
    except ValueError as e:
        print(f"Error: {e}");



async def print_user_async():
    file_path = './user.json';
    # load file and print
    with open(file_path, 'r') as file:
        data = file.read();
        user_data = loads(data);
        for u in user_data:
            print(u);

# now do app operation paralleleo

print("Running async operations...");
async def main():
    await asyncio.gather(
        asyncio.to_thread(print_user, user),
        asyncio.to_thread(to_json, user),
        asyncio.to_thread(run_division, 10, 2)
    )

    print("Async operations completed.");
    run_division(10, 0);
    # await asyncio.gather(
    #     print_user, user,
    #     to_json, user,
    #     devide, 10, 2
    # )


asyncio.run(main());
