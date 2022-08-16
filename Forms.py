from wtforms import Form, StringField, IntegerField, BooleanField, validators, Label

class AddWhitelistUser(Form):
    username = StringField(label="Username:", validators=[
        validators.input_required(message="Username required!"), 
        validators.length(1, message="Username has to be at least 1 character long!")
        ], description="Username of Player, case-sensitive.")

class ServerPropertiesForm(Form):
    # allowFlightLbl = Label(field_id="allowFlight", text="Allow Flight")
    allowFlight = BooleanField(label="Allow Flight", validators=[validators.input_required()])
    allowNether = BooleanField(label="Allow Nether", validators=[validators.input_required()])


if __name__ == "__main__":
    spf = ServerPropertiesForm()

    for f in spf:
        print(f.label)
        print(f)
    