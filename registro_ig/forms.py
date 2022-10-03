from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length

class MovementForm(FlaskForm):
    date = DateField("Fecha", validators=[DataRequired()])
    concept = StringField("Concepto", validators=[DataRequired(), Length(min=4, message= "Mas de 4 caracteres, por favor")])
    quantity = FloatField("Cantidad", validators=[DataRequired()])

    submit = SubmitField("Aceptar")