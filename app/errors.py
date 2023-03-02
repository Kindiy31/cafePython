import datetime


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass


def checkVaccine(visitor):
    try:

        # Якщо користувач не був щеплений:

        vaccine = visitor.get('vaccine')
        if not vaccine:
            raise NotVaccinatedError('NotVaccinatedError')
        # Якщо вакцина застаріла:
        expiration_date = vaccine.get('expiration_date')

        if expiration_date:
            timeNow = datetime.datetime.now().date()
            if expiration_date < timeNow:
                raise OutdatedVaccineError("OutdatedVaccineError")
        wearing_a_mask = visitor.get('wearing_a_mask')
        if wearing_a_mask is not True:
            raise NotWearingMaskError('NotWearingMaskError')

        return True
    except Exception as ve:
        raise ve
