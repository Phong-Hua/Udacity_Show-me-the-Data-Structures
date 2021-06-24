"""
Active Directory

In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. 
Where User is represented by str representing their ids. 
"""
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

"""
Write a function that provides an efficient look up of whether the user is in a group. 
"""
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if not user:
        return False

    users = group.get_users()
    for group_user in users:
        if group_user == user:
            return True;
    
    sub_groups = group.get_groups()
    for sub_group in sub_groups:
        if is_user_in_group(user, sub_group):
            return True
    
    return False;


def test_case_1():
    """
    Normal test case. User is in the group
    """
    print("************Test_case_1****************")
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_child_user, parent))
    # True

def test_case_2():
    """
    Edge test case. User does not have any parent
    """
    print("************Test_case_2****************")
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_child_user, parent))
    # False

def test_case_3():
    """
    Edge test case. User is None
    """
    print("************Test_case_3****************")
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = None
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_child_user, parent))
    # False

def test_case_4():
    """
    Edge test case. Group is invalid.
    
    """
    print("************Test_case_4****************")
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    invalid_group = Group("Invalid")

    sub_child_user = "sub_child_user"
    invalid_group.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    
    # invalid_group does not belong to parent group, but we search for sub_child_user from parent group.
    print(is_user_in_group(sub_child_user, parent))
    # False

test_case_1()
test_case_2()
test_case_3()
test_case_4()