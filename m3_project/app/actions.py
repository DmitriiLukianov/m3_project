from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow, BaseEditWindow
from m3_ext.ui import all_components as ext

from django.contrib.auth.models import User, ContentType, Group, Permission


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            label=u'last login',
            name='last_login',
            allow_blank=False,
            anchor='100%',
            format='d.m.Y')

        self.field__superuser_status = ext.ExtCheckBox(
            label=u'superuser status',
            name='is_superuser',
            allow_blank=False,
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label=u'first name',
            name='first_name',
            allow_blank=False,
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label=u'last name',
            name='last_name',
            allow_blank=False,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'email address',
            name='email',
            allow_blank=False,
            anchor='100%')

        self.field__is_staff = ext.ExtCheckBox(
            label=u'staff status',
            name='is_staff',
            allow_blank=False,
            anchor='100%')

        self.field__is_active = ext.ExtCheckBox(
            label=u'active',
            name='active',
            allow_blank=False,
            anchor='100%',)

        self.field__date_joined = ext.ExtDateField(
            label=u'date joined',
            name='date joined',
            allow_blank=False,
            anchor='100%',
            format='d.m.Y')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__superuser_status,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_staff,
            self.field__is_active,
            self.field__date_joined,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class PermissionAddWindow(BaseEditWindow):

    def _init_components(self):
        super(PermissionAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__content_type = ext.ExtDictSelectField(
            name='content_type_id',
            label='content type',
            anchor='100%',
            hide_edit_trigger=True,
            hide_trigger=True,
            hide_clear_trigger=True,
            value_field='id',
            display_field='display',
            allow_blank=False,
            editable=False,
            pack=ContentTypePack,
        )

        self.field__codename = ext.ExtStringField(
            label=u'codename',
            name='codename',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))

    def set_params(self, params):
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'


class ContentTypePack(ObjectPack):

    model = ContentType

    add_window = edit_window = ModelEditWindow.fabricate(model)

    add_to_menu = True


class UserPack(ObjectPack):

    model = User

    add_window = UserAddWindow

    edit_window = ModelEditWindow.fabricate(model)

    add_to_menu = True


class GroupPack(ObjectPack):

    model = Group

    add_window = edit_window = ModelEditWindow.fabricate(model)

    add_to_menu = True


class PermissionPack(ObjectPack):

    model = Permission

    add_window = edit_window = PermissionAddWindow

    add_to_menu = True
