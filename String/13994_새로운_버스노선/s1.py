for t in range(1, int(input()) + 1):
    cnt_arr = [0] * 1001
    n = int(input())
    for _ in range(n):
        bus_type, a, b = map(int, input().split())

        if bus_type == 1:
            for stop_idx in range(a, b):
                cnt_arr[stop_idx] += 1
        elif bus_type == 2:
            for stop_idx in range(a, b, 2):
                cnt_arr[stop_idx] += 1
        else:
            for stop_idx in range(a + 1, b):
                if not a % 2 and stop_idx % 4 == 0:
                    cnt_arr[stop_idx] += 1
                elif a % 2 and (stop_idx % 3 == 0 and stop_idx % 10 != 0):
                    cnt_arr[stop_idx] += 1
            cnt_arr[a] += 1
        cnt_arr[b] += 1

    print(f'#{t}', max(cnt_arr))
