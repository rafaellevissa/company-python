from marshmallow import Schema, fields, validate

class SetCompanySchema(Schema):
    cnpj = fields.Str(required=True, validate=validate.Length(min=14, max=14))
    cnae = fields.Str(required=True, validate=validate.Length(min=7, max=7))
    company_name = fields.Str(required=True, validate=validate.Length(min=1))
    fantasy_name = fields.Str(required=True, validate=validate.Length(min=1))
