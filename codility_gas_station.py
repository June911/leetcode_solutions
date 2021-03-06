"""
Problem Description:
1. A queue of N cars waiting at a filling station ==> A = [10, 2, 3, ...]
2. 3 Fuel dispensers ==> X, Y, Z

==> Find maximum waiting time for a car
- If more than one dispenser have the required liters, choose the one labeled the smallest number
- Tanking 1 litre ==> 1 second
- Moving car ==> 0 second
- if any car is unable to fill, return -1

"""


def solution(A, X, Y, Z):
    # write your code in Python 3.6

    # A ==> fuel demands in liters for subsequent cars in the queue
    # X,Y,Z ==> initial amount of fuel

    # initialize dispenser status
    dispenser = {
        "X": True,
        "Y": True,
        "Z": True
    }

    # remaining
    dispenser_rem = {
        "X": 0,
        "Y": 0,
        "Z": 0
    }

    time_count = 0
    while len(A) > 0:
        print("----")
        # check if dispenser is free
        min_gas = min(A)

        # check if at least one have enough gas
        if min_gas > max(X, Y, Z):
            return -1

        # if dispenser not free, we reduce all gas
        if (not dispenser["X"]) and (X >= 0):
            X -= 1
            dispenser_rem["X"] -= 1
            if (dispenser_rem["X"] == 0) and (X >= min_gas):
                dispenser["X"] = True

        if (not dispenser["Y"]) and (Y >= 0):
            Y -= 1
            dispenser_rem["Y"] -= 1
            if (dispenser_rem["Y"] == 0) and (Y >= min_gas):
                dispenser["Y"] = True

        # occupied and has remaining gas
        if (not dispenser["Z"]) and (Z > 0):
            Z -= 1
            dispenser_rem["Z"] -= 1
            if (dispenser_rem["Z"] == 0) and (Z >= min_gas):
                dispenser["Z"] = True

        # final count for max waiting time
        time_count += 1
        print(time_count, A)
        print(dispenser)
        print(dispenser_rem)
        print(X, Y, Z)

        i = 0
        # check if empty dispenser
        # no gas or no enough gas are also considered occupied
        while sum(dispenser.values()) > 0:
            # check fisrt one
            if A[i] <= X and dispenser["X"]:
                # X -= 1
                dispenser["X"] = False
                dispenser_rem["X"] = A[i]
                A.pop(i)
            else:
                # check second one
                if A[i] <= Y and dispenser["Y"]:
                    # Y -= 1
                    dispenser["Y"] = False
                    dispenser_rem["Y"] = A[i]
                    A.pop(i)
                else:
                    # check third one
                    if A[i] <= Z and dispenser["Z"]:
                        # Z -= 1
                        dispenser["Z"] = False
                        dispenser_rem["Z"] = A[i]
                        A.pop(i)
                    else:
                        # need to wait
                        # lst_wait.append(A[i])
                        i += 1
                        print("wait")

        print(time_count, A)
        print(dispenser)
        print(dispenser_rem)
        print(X, Y, Z)

    return time_count - 1


if __name__ == "__main__":
    A = [2, 8, 4, 3, 2]
    X = 7
    Y = 11
    Z = 3

    assert solution(A, X, Y, Z) == 8
    assert solution([5], 0, 4, 3) == -1
