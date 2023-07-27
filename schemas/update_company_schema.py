from marshmallow import Schema, fields, validate

class UpdateCompanySchema(Schema):
    cnae = fields.Str(required=False, validate=validate.Length(min=7, max=7))
    fantasy_name = fields.Str(required=False, validate=validate.Length(min=1))