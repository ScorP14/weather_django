def convert_gradus_in_side_horizon(gradus: float):
    if gradus > 360:
        raise ValueError()
    return {
        0 <= gradus < 22.5: 'C',
        22.5 <= gradus < 67.5: 'CВ',
        67.5 <= gradus < 112.5: 'В',
        112.5 <= gradus < 157.5: 'ЮВ',
        157.5 <= gradus < 202.5: 'Ю',
        202.5 <= gradus < 247.5: 'ЮЗ',
        247.5 <= gradus < 292.5: 'З',
        292.5 <= gradus < 337.5: 'СЗ',
        337.5 <= gradus <= 360: 'C',
    }[True]

