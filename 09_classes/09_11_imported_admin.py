from admin import User, Privileges, Admin

admin = Admin('Heidy', 'Navarrete', 'Albright', '19', ['can ban user', 'can delete post'])
admin.describe_user()
admin.privileges.show_privileges()