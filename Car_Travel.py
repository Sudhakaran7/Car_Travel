class Validate(object):
    def Car_travel(self, people, seat):
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= seat:
                i += 1
            j -= 1
        return ans
val=Validate()
people=list(map(int,input().split()))
seat=int(input())
print(val.Car_travel(people,seat))
