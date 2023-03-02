from app.errors import NotVaccinatedError, NotWearingMaskError, \
    OutdatedVaccineError


def go_to_cafe(friends, cafe):
    needMask = 0
    vaccineError = False
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except Exception as a:
            classExcept = (a.__class__)
            if classExcept == NotWearingMaskError:
                needMask += 1
            elif classExcept == NotVaccinatedError or \
                    classExcept == OutdatedVaccineError:
                vaccineError = True
                break
    if vaccineError is True:
        return 'All friends should be vaccinated'
    elif needMask > 0:
        return f'Friends should buy {needMask} masks'
    else:
        return 'Friends can go to KFC'
