# заполнение массива числами
num = list(map(int, input('Введите числа через пробел: ').split()))
nums = sorted(num)
cnt = 0
med = int(sum(nums) / len(nums))
# подсчет количества ходов
while nums[0] != nums[-1] :
    for i in range(len(nums)):
        if nums[i] < med :
            nums[i] = nums[i] + 1
            cnt += 1
        elif nums[i] > med:
            nums[i] = nums[i] - 1
            cnt += 1
print(f'Минимальное количество ходов - {cnt}')