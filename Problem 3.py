n = int(input())
codes = list(map(int, input().split()))
d = [0]*1001

def process_country_codes(n, codes):
    try:
        assert all(number >=0 for number in codes)

        for i in range(n):
            if d[codes[i]] == 0:
                print(codes[i], end = ' ')
                d[codes[i]] = 1
        print()
    except AssertionError:
        print("Negative country codes are not allowed.")
    finally:
        print("Processing Completed.")


process_country_codes(n, codes) 