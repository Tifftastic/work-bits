# file: create-fields.py

with open('newFieldsXML.txt','w') as newFieldsFile:

    list_name = ['Application_Year','LRS_CountiesServed','Full_Time_Staff','Part_Time_Staff','Num_Attorney_Members','Num_Governing_Members','Num_Referrals','Num_SubjectMatterPanels','Modest_Means_Panel','Compliance_Rule125','Num_ModestMeansServed','ClientSurveyResults','FreeLegalServices','ReducedFee_LegalServices','FreeLegalAdvice_ClearingHouseServices','OtherEfforts_ProBonoPrograms','TB_Fees','RecertificationFeePaid','RecertificationFeeWaived','Annual_Membership_Fee','Annual_Subject_Matter_Panel_Fee','Forwarding_Percentage_Fee','Initial_Consultation_Client_Referral_Fee','Other_Fees_Charged','TB_Financials','Financial_Reserves','Deficit','Waivers','Deficiencies','Membership_Fees','Panel_Fees_no_separate_membership_fee','Percentage_Fees','Referral_Fees','Other_Fees_Charged_Num','Other_Revenues','Salaries_Staff_Expenses','Rent','Advertising','Operating_Expenses','Capital_Expenditures','Other_Expenditures','Gross_Annnual_Revenue','Gross_Annual_Expenses','Net_Income','Notes']

    for index,item in enumerate(list_name,1):
        newFieldsFile.write("""
        <customfield>
	    <displayorder>{}</displayorder>
	    <name>{}</name>
        <tabname></tabname>
	   <type>30</type>
	   <options></options><validationtype>0</validationtype>
	   <allowempty>1</allowempty>
	   <numformat></numformat>
	   <formatxml>&lt;size&gt;Large&lt;/size&gt;
        &lt;style&gt;&lt;/style&gt;&lt;tooltip&gt;&lt;/tooltip&gt;&lt;msg&gt;&lt;/msg&gt;&lt;upf&gt;&lt;/upf&gt;&lt;wvp&gt;,&lt;/wvp&gt;&lt;maxp&gt;0&lt;/maxp&gt;&lt;xmlshowclear&gt;0&lt;/xmlshowclear&gt;&lt;mapstrokeweight&gt;2&lt;/mapstrokeweight&gt;
	</formatxml>
	<vlogic></vlogic>
	<caption></caption>
	<cusvalidation></cusvalidation>
	<cusdesp></cusdesp></customfield>\n""".format(index*10,item))

filename = 'file:///Users/RubbaDubDub/GitHub/work-bits' + '/newFieldsXML.txt'
