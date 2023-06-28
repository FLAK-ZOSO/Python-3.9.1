from __future__ import annotations
import random
import asyncio


class Student:
    # __slots__: tuple[str, str] = ('name', 'age')
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f'<Student name={self.name} age={self.age}>'

    def __str__(self) -> str:
        return f'{self.name} ({self.age})'

    def __eq__(self, other: Student) -> bool:
        return self.name == other.name and self.age == other.age


async def async_func() -> None:
    print('Hello')
    await asyncio.sleep(1)
    print('World')

async def main() -> None:
    c = async_func()
    print('Done')
    await c

def fibonacci_generator() -> int:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

if __name__ == '__main__':
    ...
    s: Student = Student('Giacomo', 17)
    s2: Student = Student('Mattia', 18)

    ls = [s, s2]
    for i in range(0, 98):
        ls.append(
            Student(
                f'Person{i}',
                random.randint(0, 100)
            )
        )

    sum_age = sum([s.age for s in ls])
    average = sum_age / len(ls)
    print(f'Average age: {average}')

    print(f'Average age: {average:.1f} (rounded)')
    print('Average age: {:.1f} (rounded)'.format(average))
    print('Average age: %.1f (rounded)' % average)
    print('Average age: ' + str(round(average, 1)) + ' (rounded)')

    asyncio.run(main())