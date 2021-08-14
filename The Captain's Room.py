k = int(input())
room_list = list(map(int, input().split()))
a = set(room_list)
for item in a:
    room_list.remove(item)
room_set = set(room_list)
capt_room = list(a - room_set)[0]
print(capt_room)