
# import mysql.connector


OstrichUplod_Path="/home/deepak/PycharmProjects/cginclusionh3I/OstrichUploderFolder/"                            # TODO: Replace with the Ostrich Uplod path input location

SourceFile_Path="/home/deepak/PycharmProjects/cginclusionh3I/SourceFolder/"                                      # TODO: Replace with the Soure file path input location


Days_To_Subtract= 1                                 # TODO: Days to substract from the current day

Columns_Taken=03,04,35                                # TODO: columns taken from the .csv file


sql_select_Query_NonTrigger_Updates = "select o.ENTITY_ID from control_group c left join registration_list r on c.registration_list_id=r.registration_list_id left join partner p on c.reference_entity_id=p.event_instance_id left join oz_entity o on r.registration_list_id=o.external_reference_id where c.deleted=0 and p.partner_id=1 and o.ENTITY_TYPE_ID=3"

PercentageGeneration='50'               # TODO: change the percentage randon number generation value

# AddCountryCodeValue="091"            # TODO: add Country code value infront of msisdn (optional)
