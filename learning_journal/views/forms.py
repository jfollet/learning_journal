from wtforms import Form, TextAreaField, validators, PasswordField, StringField


def strip_filter(x):
    return x.strip() if x else None


class EntryForm(Form):
    title = StringField('Entry Title',
                      [validators.Length(min=1, max=255)],
                      filters=[strip_filter]
                      )
    body = TextAreaField('Entry Body',
                         [validators.Length(min=1)],
                         filters=[strip_filter]
                         )

class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=255)])
    password = PasswordField('Password', [validators.Length(min=1, max =255)])
