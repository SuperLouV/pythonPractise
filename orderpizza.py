pizza = {
    '底': ['厚', '薄'],
    '料': ['蘑菇', '芝士'],
}
print("请输入1选厚底，2选薄底")
a = input()
if a == '1':
    a = '厚'
    print("您选择了厚底")
elif a == '2':
    a = '薄'
    print("您选择了薄底")
print("请输入1选蘑菇，2选芝士")
b = input()
if b == '1':
    b = '蘑菇'
    print("您选择了蘑菇")
elif b == '2':
    b = '芝士'
    print("您选择了芝士")
print("您选择了"+a+"底加"+b+"的披萨")
