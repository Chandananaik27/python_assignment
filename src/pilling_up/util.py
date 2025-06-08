def can_stack_cubes(num_cubes, cube_lengths):
    left = 0
    right = num_cubes - 1
    prev_cube = float('inf')

    while left <= right:
        if cube_lengths[left] > cube_lengths[right]:
            current_cube = cube_lengths[left]
            left += 1
        else:
            current_cube = cube_lengths[right]
            right -= 1

        if current_cube > prev_cube:
            return "No"

        prev_cube = current_cube

    return "Yes"


def main():
    num_test_cases = int(input().strip())

    for _ in range(num_test_cases):
        num_cubes = int(input().strip())
        cube_lengths = list(map(int, input().strip().split()))
        print(can_stack_cubes(num_cubes, cube_lengths))