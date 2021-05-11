# Generated by Django 3.2 on 2021-05-04 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210429_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('AOK', 'AOK'), ('MDL', 'MDL'), ('CHW', 'CHW'), ('CYP', 'CYP'), ('MRO', 'MRO'), ('MAF', 'MAF'), ('MZM', 'MZM'), ('BND', 'BND'), ('CVE', 'CVE'), ('MVR', 'MVR'), ('ZMK', 'ZMK'), ('SAR', 'SAR'), ('KYD', 'KYD'), ('MRU', 'MRU'), ('CHE', 'CHE'), ('THB', 'THB'), ('CNH', 'CNH'), ('LVR', 'LVR'), ('CUP', 'CUP'), ('STN', 'STN'), ('GRD', 'GRD'), ('ECS', 'ECS'), ('MTP', 'MTP'), ('XBC', 'XBC'), ('MUR', 'MUR'), ('XUA', 'XUA'), ('CNY', 'CNY'), ('WST', 'WST'), ('ANG', 'ANG'), ('HKD', 'HKD'), ('ILP', 'ILP'), ('MDC', 'MDC'), ('ZAR', 'ZAR'), ('ATS', 'ATS'), ('PES', 'PES'), ('VEF', 'VEF'), ('BIF', 'BIF'), ('MMK', 'MMK'), ('XFU', 'XFU'), ('XRE', 'XRE'), ('SHP', 'SHP'), ('BGL', 'BGL'), ('TPE', 'TPE'), ('XAG', 'XAG'), ('JMD', 'JMD'), ('TMM', 'TMM'), ('HNL', 'HNL'), ('UYI', 'UYI'), ('PEI', 'PEI'), ('AWG', 'AWG'), ('QAR', 'QAR'), ('RHD', 'RHD'), ('MXV', 'MXV'), ('MOP', 'MOP'), ('ZRN', 'ZRN'), ('HUF', 'HUF'), ('BDT', 'BDT'), ('BAM', 'BAM'), ('AFN', 'AFN'), ('PEN', 'PEN'), ('GEL', 'GEL'), ('ZWR', 'ZWR'), ('DEM', 'DEM'), ('BOB', 'BOB'), ('EUR', 'EUR'), ('BYN', 'BYN'), ('ARL', 'ARL'), ('AOR', 'AOR'), ('LAK', 'LAK'), ('HTG', 'HTG'), ('LTT', 'LTT'), ('ITL', 'ITL'), ('UYW', 'UYW'), ('YDD', 'YDD'), ('PAB', 'PAB'), ('TJS', 'TJS'), ('NIO', 'NIO'), ('XEU', 'XEU'), ('XPF', 'XPF'), ('BGN', 'BGN'), ('XAU', 'XAU'), ('KES', 'KES'), ('PLZ', 'PLZ'), ('XSU', 'XSU'), ('ZWD', 'ZWD'), ('YUN', 'YUN'), ('FIM', 'FIM'), ('GNF', 'GNF'), ('LTL', 'LTL'), ('XTS', 'XTS'), ('AON', 'AON'), ('ILR', 'ILR'), ('MCF', 'MCF'), ('DOP', 'DOP'), ('KPW', 'KPW'), ('EGP', 'EGP'), ('ALL', 'ALL'), ('MXN', 'MXN'), ('SRD', 'SRD'), ('SRG', 'SRG'), ('ERN', 'ERN'), ('BEF', 'BEF'), ('OMR', 'OMR'), ('AUD', 'AUD'), ('XAF', 'XAF'), ('MGF', 'MGF'), ('ALK', 'ALK'), ('MGA', 'MGA'), ('HRD', 'HRD'), ('FRF', 'FRF'), ('INR', 'INR'), ('JPY', 'JPY'), ('AZM', 'AZM'), ('CNX', 'CNX'), ('TTD', 'TTD'), ('UAK', 'UAK'), ('UYP', 'UYP'), ('ZRZ', 'ZRZ'), ('ESA', 'ESA'), ('CLE', 'CLE'), ('FJD', 'FJD'), ('BUK', 'BUK'), ('USS', 'USS'), ('DJF', 'DJF'), ('SUR', 'SUR'), ('NOK', 'NOK'), ('KHR', 'KHR'), ('VNN', 'VNN'), ('COU', 'COU'), ('AZN', 'AZN'), ('MKD', 'MKD'), ('ZAL', 'ZAL'), ('BOP', 'BOP'), ('TWD', 'TWD'), ('AFA', 'AFA'), ('SSP', 'SSP'), ('BOV', 'BOV'), ('VEB', 'VEB'), ('VUV', 'VUV'), ('PHP', 'PHP'), ('XXX', 'XXX'), ('CSK', 'CSK'), ('LVL', 'LVL'), ('ESP', 'ESP'), ('GQE', 'GQE'), ('KGS', 'KGS'), ('MKN', 'MKN'), ('LYD', 'LYD'), ('RUR', 'RUR'), ('BRZ', 'BRZ'), ('BMD', 'BMD'), ('BEC', 'BEC'), ('GWE', 'GWE'), ('SDD', 'SDD'), ('GHC', 'GHC'), ('KMF', 'KMF'), ('PGK', 'PGK'), ('BTN', 'BTN'), ('GIP', 'GIP'), ('BBD', 'BBD'), ('SLL', 'SLL'), ('YER', 'YER'), ('KZT', 'KZT'), ('GNS', 'GNS'), ('RWF', 'RWF'), ('GTQ', 'GTQ'), ('XBA', 'XBA'), ('MZE', 'MZE'), ('LUL', 'LUL'), ('PKR', 'PKR'), ('ESB', 'ESB'), ('BWP', 'BWP'), ('TRY', 'TRY'), ('TJR', 'TJR'), ('YUD', 'YUD'), ('HRK', 'HRK'), ('ARM', 'ARM'), ('COP', 'COP'), ('SBD', 'SBD'), ('SKK', 'SKK'), ('USN', 'USN'), ('BHD', 'BHD'), ('BOL', 'BOL'), ('UYU', 'UYU'), ('BEL', 'BEL'), ('AED', 'AED'), ('MYR', 'MYR'), ('DDM', 'DDM'), ('FKP', 'FKP'), ('KWD', 'KWD'), ('GEK', 'GEK'), ('ARA', 'ARA'), ('NLG', 'NLG'), ('RSD', 'RSD'), ('GYD', 'GYD'), ('CUC', 'CUC'), ('NAD', 'NAD'), ('XPD', 'XPD'), ('BZD', 'BZD'), ('UGX', 'UGX'), ('XPT', 'XPT'), ('NPR', 'NPR'), ('DZD', 'DZD'), ('TOP', 'TOP'), ('XBB', 'XBB'), ('TZS', 'TZS'), ('BGO', 'BGO'), ('CSD', 'CSD'), ('PLN', 'PLN'), ('RON', 'RON'), ('BRE', 'BRE'), ('SVC', 'SVC'), ('BGM', 'BGM'), ('BYR', 'BYR'), ('CAD', 'CAD'), ('LRD', 'LRD'), ('SGD', 'SGD'), ('USD', 'USD'), ('ZWL', 'ZWL'), ('MAD', 'MAD'), ('LSL', 'LSL'), ('ETB', 'ETB'), ('PYG', 'PYG'), ('XFO', 'XFO'), ('ECV', 'ECV'), ('BAN', 'BAN'), ('MTL', 'MTL'), ('BRR', 'BRR'), ('SZL', 'SZL'), ('BYB', 'BYB'), ('XBD', 'XBD'), ('IEP', 'IEP'), ('ILS', 'ILS'), ('TMT', 'TMT'), ('GMD', 'GMD'), ('SDP', 'SDP'), ('BRN', 'BRN'), ('AOA', 'AOA'), ('XCD', 'XCD'), ('GHS', 'GHS'), ('GBP', 'GBP'), ('LKR', 'LKR'), ('IQD', 'IQD'), ('NIC', 'NIC'), ('STD', 'STD'), ('MZN', 'MZN'), ('MWK', 'MWK'), ('CLP', 'CLP'), ('SEK', 'SEK'), ('ISK', 'ISK'), ('ARP', 'ARP'), ('RUB', 'RUB'), ('LBP', 'LBP'), ('CZK', 'CZK'), ('LUF', 'LUF'), ('ADP', 'ADP'), ('MXP', 'MXP'), ('NZD', 'NZD'), ('PTE', 'PTE'), ('CRC', 'CRC'), ('YUR', 'YUR'), ('IDR', 'IDR'), ('SDG', 'SDG'), ('VES', 'VES'), ('VND', 'VND'), ('EEK', 'EEK'), ('SCR', 'SCR'), ('BSD', 'BSD'), ('KRW', 'KRW'), ('SYP', 'SYP'), ('DKK', 'DKK'), ('BAD', 'BAD'), ('MNT', 'MNT'), ('BRL', 'BRL'), ('ISJ', 'ISJ'), ('MVP', 'MVP'), ('NGN', 'NGN'), ('GWP', 'GWP'), ('CHF', 'CHF'), ('ARS', 'ARS'), ('IRR', 'IRR'), ('CLF', 'CLF'), ('LUC', 'LUC'), ('SIT', 'SIT'), ('KRH', 'KRH'), ('XDR', 'XDR'), ('KRO', 'KRO'), ('YUM', 'YUM'), ('ROL', 'ROL'), ('UAH', 'UAH'), ('ZMW', 'ZMW'), ('BRC', 'BRC'), ('MLF', 'MLF'), ('TND', 'TND'), ('SOS', 'SOS'), ('JOD', 'JOD'), ('CDF', 'CDF'), ('BRB', 'BRB'), ('XOF', 'XOF'), ('AMD', 'AMD'), ('UGS', 'UGS'), ('UZS', 'UZS'), ('TRL', 'TRL')], default='USD', max_length=3),
        ),
    ]