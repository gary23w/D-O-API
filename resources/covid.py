from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.covid import CovidModel

        # 'name': self.name,
        #  'confirmed': self.confirmed,
        #  'recovered': self.recovered,
        #  'critical': self.critical,
        #  'deaths': self.deaths,
        #  'last_update': self.last_update

class Covid(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('confirmed',
        type=str,
        required=True,
        help="confirmed"
    )
    parser.add_argument('recovered',
        type=str,
        required=True,
        help="recovered"
    )
    parser.add_argument('critical',
        type=str,
        required=True,
        help="critical"
    )
    parser.add_argument('deaths',
        type=str,
        required=True,
        help="deaths"
    )
    parser.add_argument('last_update',
        type=str,
        required=True,
        help="last_update"
    )


    def get(self, name):
        covid = CovidModel.find_by_name(name)
        if covid:
            return covid.json()
        return {'message': 'Not found'}, 404

    @jwt_required()
    def post(self, name):
        if CovidModel.find_by_name(name):
            return {'message': " name '{}' already exists.".format(name)}, 400

        data = Covid.parser.parse_args()

        covid = CovidModel(name, **data)

        try:
            covid.save_to_db()
        except:
            return {"message": "An error occurred inserting covid"}, 500

        return item.json(), 201

    def delete(self, name):
        covid = CovidModel.find_by_name(name)
        if covid:
            covid.delete_from_db()

        return {'message': 'covid deleted???????????'}


class CovidList(Resource):
    def get(self):
        return {'stuff': [x.json() for x in CovidModel.query.all()]}
