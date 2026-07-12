import asyncio
from json import loads, dumps;
from service import get_user;
from utils import print_user, to_json, divide;




def user():
    user = get_user(1);
    if user is None:
        print("User not found");
        return;
    print_user(user);
    json_result = to_json(user);
    print(json_result);




def run_division(a, b):
    try:
        result = divide(a, b);
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
        asyncio.to_thread(user),
        asyncio.to_thread(run_division, 10, 2)
    )

    print("Async operations completed.");
    run_division(10, 0);
    user()


asyncio.run(main());

