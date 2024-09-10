import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl


# Generate universe variables
def larsen(my_market_value, my_location,my_asset, my_income, my_interest):

    market_value = np.arange(0, 1100, 50)
    location = np.arange(0, 11, 0.5)
    asset = np.arange(0, 1100, 50)
    income =np.arange(0, 110, 5)
    interest = np.arange(0, 11,0.5)

    house = np.arange(0,11,1)
    applicant = np.arange(0,11,1)
    credit = np.arange(0,550,25)



    # Generate fuzzy membership functions
    market_valueL_mf = fuzz.trapmf(market_value, [0,0,50,100])
    market_valueM_mf = fuzz.trapmf(market_value, [50,100, 200,250])
    market_valueH_mf = fuzz.trapmf(market_value, [200,300,650,850])
    market_valueVH_mf = fuzz.trapmf(market_value, [650,850,1000,1000])

    locationB_mf = fuzz.trapmf(location , [0,0,1.5,4])
    locationF_mf  = fuzz.trapmf(location , [2.5 , 5 , 6, 8.5])
    locationE_mf  = fuzz.trapmf(location , [6,8.5,10,10])

    houseVL_mf = fuzz.trimf(house, [0,0,3])
    houseL_mf = fuzz.trimf(house, [0,3,6])
    houseM_mf = fuzz.trimf(house, [2,5,8])
    houseH_mf = fuzz.trimf(house, [4,7,10])
    houseVH_mf = fuzz.trimf(house, [7,10,10])

    assetL_mf = fuzz.trapmf(asset, [0,0,0,150])
    assetM_mf = fuzz.trapmf(asset, [50,250,450,650])
    assetH_mf = fuzz.trapmf(asset, [500,700,1000,1000])

    incomeL_mf = fuzz.trapmf(income, [0,0,10,25])
    incomeM_mf = fuzz.trapmf(income, [15,35,35,55])
    incomeH_mf = fuzz.trapmf(income, [40,60,60,80])
    incomeVH_mf = fuzz.trapmf(income, [60,80,100,100])

    interestL_mf = fuzz.trapmf(interest, [0,0,2,5])
    interestM_mf = fuzz.trapmf(interest, [2,4,6,8])
    interestH_mf = fuzz.trapmf(interest, [6,8.5,10,10])

    applicantL_mf = fuzz.trapmf(applicant, [0,0,2,4])
    applicantM_mf = fuzz.trapmf(applicant, [2,5,5,8])
    applicantH_mf = fuzz.trapmf(applicant, [6,8,10,10])

    creditVL_mf = fuzz.trimf(credit, [0,0,125])
    creditL_mf = fuzz.trimf(credit, [0,125,250])
    creditM_mf = fuzz.trimf(credit, [125,250,375])
    creditH_mf = fuzz.trimf(credit, [250,375,500])
    creditVH_mf = fuzz.trimf(credit, [375,500,500])




    # interpolated discrete membership function at specific value
    market_valueL = fuzz.interp_membership(market_value, market_valueL_mf , my_market_value)
    market_valueM = fuzz.interp_membership(market_value, market_valueM_mf , my_market_value)
    market_valueH = fuzz.interp_membership(market_value, market_valueH_mf , my_market_value)
    market_valueVH = fuzz.interp_membership(market_value, market_valueVH_mf , my_market_value)

    locationB = fuzz.interp_membership(location, locationB_mf, my_location)
    locationF = fuzz.interp_membership(location, locationF_mf, my_location)
    locationE = fuzz.interp_membership(location, locationE_mf, my_location)

    assetL = fuzz.interp_membership(asset, assetL_mf, my_asset)
    assetM = fuzz.interp_membership(asset, assetM_mf, my_asset)
    assetH = fuzz.interp_membership(asset, assetH_mf, my_asset)

    incomeL = fuzz.interp_membership(income, incomeL_mf, my_income)
    incomeM = fuzz.interp_membership(income, incomeM_mf, my_income)
    incomeH = fuzz.interp_membership(income, incomeH_mf, my_income)
    incomeVH = fuzz.interp_membership(income, incomeVH_mf, my_income)

    interestL = fuzz.interp_membership( interest, interestL_mf, my_interest )
    interestM = fuzz.interp_membership( interest, interestM_mf, my_interest )
    interestH = fuzz.interp_membership( interest, interestH_mf, my_interest )





    # Now we take our rules and apply them.
    locationBad_MarketMedium = np.dot(locationB, market_valueM)
    locationFair_MarketLow = np.dot(locationF , market_valueL)
    locationBad_MarketLow = np.dot(locationB, market_valueL)
    locationBad_marketHigh = np.dot(locationB, market_valueH)
    locationFair_marketMedium = np.dot(locationF, market_valueM)
    locationEx_marketLow = np.dot(locationE , market_valueL)
    locationBad_marketVeryHigh = np.dot(locationB, market_valueVH)
    locationFair_marketHigh = np.dot(locationF, market_valueH)
    locationEx_marketMedium = np.dot(locationE, market_valueM)
    locationFair_marketVeryHigh = np.dot(locationF, market_valueVH)
    locationEx_marketHigh = np.dot(locationE, market_valueH)
    locationEx_marketVeryHigh = np.dot(locationE, market_valueVH)
    ####################################
    assetLow_incomeLow = np.dot(assetL , incomeL)
    assetLow_incomeMedium = np.dot(assetL, incomeM)
    assetMedium_incomeLow = np.dot(assetM, incomeL)
    assetLow_incomeHigh = np.dot(assetL , incomeH)
    assetMedium_incomeMedium = np.dot(assetM , incomeM)
    assetHigh_incomeLow = np.dot(assetH , incomeL)
    assetHigh_incomeMedium = np.dot(assetH, incomeM)
    assetLow_incomeVeryHigh = np.dot(assetL, incomeVH)
    assetMedium_incomeHigh = np.dot(assetM , incomeH)
    assetMedium_incomeVeryHigh = np.dot(assetM , incomeVH)
    assetHigh_incomeHigh = np.dot(assetH , incomeH )
    assetHigh_incomeVeryHigh = np.dot(assetH , incomeVH)

    # Now we apply a product operation for the larsen Inference method
    # membership function with `np.dot`
    house_low1 = np.dot(locationBad_MarketMedium, houseL_mf) # removed entirely to 0
    house_low2 = np.dot(market_valueL, houseL_mf)
    house_low3 = np.dot(locationB , houseL_mf)
    house_low4 = np.dot(locationFair_MarketLow , houseL_mf)
    house_very_low = np.dot(locationBad_MarketLow , houseVL_mf)
    house_medium1 = np.dot(locationBad_marketHigh, houseM_mf)
    house_medium2 = np.dot(locationFair_marketMedium, houseM_mf)
    house_medium3 = np.dot(locationEx_marketLow, houseM_mf)
    house_high1 = np.dot(locationBad_marketVeryHigh, houseH_mf)
    house_high2 = np.dot(locationFair_marketHigh, houseH_mf)
    house_high3 = np.dot(locationEx_marketMedium, houseH_mf)
    house_very_high1 = np.dot(locationFair_marketVeryHigh, houseVH_mf)
    house_very_high2 = np.dot(locationEx_marketHigh, houseVH_mf)
    house_very_high3 = np.dot(locationEx_marketVeryHigh, houseVH_mf)
    ####################################
    applicant_low1 = np.dot(assetLow_incomeLow, applicantL_mf)
    applicant_low2 = np.dot(assetLow_incomeMedium , applicantL_mf)
    applicant_low3 = np.dot(assetMedium_incomeLow, applicantL_mf)
    applicant_medium1 = np.dot(assetLow_incomeHigh, applicantM_mf)
    applicant_medium2 = np.dot(assetMedium_incomeMedium, applicantM_mf)
    applicant_medium3 = np.dot(assetHigh_incomeLow, applicantM_mf)
    applicant_medium4 = np.dot(assetHigh_incomeMedium, applicantM_mf)
    applicant_high1 = np.dot(assetLow_incomeVeryHigh, applicantH_mf)
    applicant_high2 = np.dot(assetMedium_incomeHigh , applicantH_mf)
    applicant_high3 = np.dot(assetMedium_incomeVeryHigh, applicantH_mf)
    applicant_high4 = np.dot(assetHigh_incomeHigh , applicantH_mf)
    applicant_high5 = np.dot(assetHigh_incomeVeryHigh , applicantH_mf)


    house0 = np.zeros_like(house)
    applicant0 = np.zeros_like(applicant)
    # Aggregate all three output membership functions together
    aggregated_applicant = np.fmax(applicant_low1,
                            np.fmax(applicant_low2,
                            np.fmax(applicant_low3,
                            np.fmax(applicant_medium1,
                            np.fmax(applicant_medium2,
                            np.fmax(applicant_medium3,
                            np.fmax(applicant_medium4,
                            np.fmax(applicant_high1,
                            np.fmax(applicant_high2,
                            np.fmax(applicant_high3,
                            np.fmax(applicant_high4,applicant_high5)))))))))))


    aggregated_house = np.fmax(house_low1,
                         np.fmax(house_low2,
                         np.fmax(house_low3,
                         np.fmax(house_low4,
                         np.fmax(house_very_low,
                         np.fmax(house_medium1,
                         np.fmax(house_medium2,
                         np.fmax(house_medium3,
                         np.fmax(house_high1,
                         np.fmax(house_high2,
                         np.fmax(house_high3,
                         np.fmax(house_very_high1,
                         np.fmax(house_very_high2,house_very_high3)))))))))))))




    # Calculate defuzzified result
    applicant_result = fuzz.defuzz(applicant, aggregated_applicant, 'centroid')
    applicant_result_activation = fuzz.interp_membership(applicant, aggregated_applicant, applicant_result)

    house_result = fuzz.defuzz(house, aggregated_house, 'centroid')
    house_result_activation = fuzz.interp_membership(house, aggregated_house, house_result)  # for plot
    # Visualize this
    # Visualize these universes and membership functions
    fig, ( ax3,ax4) = plt.subplots(nrows=2, figsize=(9,4))


    ax4.plot(applicant, applicantL_mf, 'g', linewidth=0.5, label='Low')
    ax4.plot(applicant, applicantM_mf, 'r', linewidth=0.5, label='Medium')
    ax4.plot(applicant, applicantH_mf, 'c', linewidth=0.5, label='High')
    ax4.fill_between(applicant, applicant0, aggregated_applicant, facecolor='Orange', alpha=0.7)
    ax4.plot([applicant_result, applicant_result], [0, applicant_result_activation], 'k', linewidth=1.5, alpha=0.9)
    ax4.plot([0, applicant_result], [applicant_result_activation, applicant_result_activation], 'k', linewidth=1.5, alpha=0.9)
    ax4.set_title('Applicant')
    ax4.text(applicant_result , applicant_result_activation ,"{}".format(int(applicant_result)))
    ax4.text(0 , applicant_result_activation,"{}".format(format(applicant_result_activation , '.2f')))
    ax4.legend()

    ax3.plot(house, houseVL_mf, 'b', linewidth=0.5,label='Very Low' )
    ax3.plot(house, houseL_mf, 'g', linewidth=0.5, label='Low')
    ax3.plot(house, houseM_mf, 'r', linewidth=0.5, label='Medium')
    ax3.plot(house, houseH_mf, 'c', linewidth=0.5, label='High')
    ax3.plot(house, houseVH_mf, 'k', linewidth=0.5,label='Very High')
    ax3.fill_between(house, house0, aggregated_house, facecolor='Orange', alpha=0.7)
    ax3.plot([house_result, house_result], [0, house_result_activation], 'k', linewidth=1.5, alpha=0.9)
    ax3.plot([0, house_result], [house_result_activation, house_result_activation], 'k', linewidth=1.5, alpha=0.9)
    ax3.set_title('House')
    ax3.text(house_result,house_result_activation,"{}".format(house_result))
    ax3.text(0 , house_result_activation,"{}".format(format(house_result_activation , '.2f')))
    ax3.legend()
    #####################

    # interpolated discrete membership function at house and applicant new values
    houseVL =  fuzz.interp_membership( house , houseVL_mf, house_result )
    houseL = fuzz.interp_membership( house , houseL_mf, house_result )
    houseM = fuzz.interp_membership( house , houseM_mf, house_result )
    houseH = fuzz.interp_membership( house , houseH_mf, house_result )
    houseVH = fuzz.interp_membership( house , houseVH_mf, house_result )

    applicantL = fuzz.interp_membership( applicant , applicantL_mf, applicant_result )
    applicantM = fuzz.interp_membership( applicant , applicantM_mf, applicant_result )
    applicantH = fuzz.interp_membership( applicant , applicantH_mf, applicant_result )


    # Now we take our rules and apply them.
    incomeLow_interestMedium = np.dot(incomeL , interestM )
    incomeLow_interestHigh = np.dot(incomeL , interestH)
    incomeMedium_interestHigh = np.dot(incomeM, interestH)
    applicantMedium_houseVeryLow = np.dot(applicantM , houseVL)
    applicantMedium_houseLow = np.dot(applicantM , houseL)
    applicantHigh_houseVeryLow = np.dot( applicantH , houseVL)
    applicantMedium_houseMedium = np.dot( applicantM , houseM )
    applicantHigh_houseLow = np.dot( applicantH , houseL )
    applicantMedium_houseHigh = np.dot( applicantM , houseH )
    applicantMedium_houseVeryHigh = np.dot( applicantM, houseVH )
    applicantHigh_houseMedium = np.dot( applicantH , houseM )
    applicantHigh_houseHigh = np.dot (applicantH , houseH)
    applicantHigh_houseVeryHigh = np.dot( applicantH , houseVH)

    # Now we apply a product operation for the larsen Inference method
    # membership function with `np.dot`
    credit_very_low1 = np.dot(incomeLow_interestMedium , creditVL_mf)
    credit_very_low2 = np.dot(incomeLow_interestHigh , creditVL_mf)
    credit_very_low3 = np.dot(applicantL , creditVL_mf)
    credit_very_low4 = np.dot(houseVL , creditVL_mf)
    credit_low1 = np.dot(incomeMedium_interestHigh , creditL_mf)
    credit_low2 = np.dot(applicantMedium_houseVeryLow , creditL_mf)
    credit_low3 = np.dot( applicantMedium_houseLow , creditL_mf)
    credit_low4 = np.dot( applicantHigh_houseVeryLow , creditL_mf )
    credit_medium1 = np.dot( applicantMedium_houseMedium , creditM_mf )
    credit_medium2 = np.dot(applicantHigh_houseLow , creditM_mf)
    credit_high1 = np.dot( applicantMedium_houseHigh , creditH_mf )
    credit_high2 = np.dot (applicantMedium_houseVeryHigh , creditH_mf)
    credit_high3 = np.dot(applicantHigh_houseMedium , creditH_mf)
    credit_high4 = np.dot (applicantHigh_houseHigh , creditH_mf)
    credit_very_high1 = np.dot (applicantHigh_houseVeryHigh , creditVH_mf)



    credit0 = np.zeros_like(credit)
    # Aggregate all three output membership functions together
    aggregated_credit = np.fmax(credit_very_low1,
                        np.fmax(credit_very_low2,
                        np.fmax(credit_very_low3,
                        np.fmax(credit_very_low4,
                        np.fmax(credit_low1,
                        np.fmax(credit_low2,
                        np.fmax(credit_low3,
                        np.fmax(credit_low4,
                        np.fmax(credit_medium1,
                        np.fmax(credit_medium2,
                        np.fmax(credit_high1,
                        np.fmax(credit_high2,
                        np.fmax(credit_high3,
                        np.fmax(credit_high4,credit_very_high1))))))))))))))



    # Calculate defuzzified result
    credit_result = fuzz.defuzz(credit, aggregated_credit, 'centroid')
    credit_result_activation = fuzz.interp_membership(credit, aggregated_credit, credit_result)


    # Visualize these universes and membership functions
    fig, ( ax5) = plt.subplots(nrows=1, figsize=(9,4))


    ax5.plot(credit, creditVL_mf, 'b', linewidth=0.5, label='very Low')
    ax5.plot(credit, creditL_mf, 'g', linewidth=0.5, label='Low')
    ax5.plot(credit, creditM_mf, 'r', linewidth=0.5, label='Medium')
    ax5.plot(credit, creditH_mf, 'c', linewidth=0.5, label='High')
    ax5.plot(credit, creditVH_mf, 'k', linewidth=0.5, label='very High')
    ax5.fill_between(credit, credit0, aggregated_credit, facecolor='Orange', alpha=0.7)
    ax5.plot([credit_result, credit_result], [0, credit_result_activation], 'k', linewidth=1.5, alpha=0.9)
    ax5.plot([0, credit_result], [credit_result_activation, credit_result_activation], 'k', linewidth=1.5, alpha=0.9)
    ax5.set_title('Credit')
    ax5.text(credit_result , credit_result_activation ,"{}".format(credit_result))
    ax5.text(0 , credit_result_activation,"{}".format(format(credit_result_activation , '.2f')))
    ax5.legend()




    plt.tight_layout()
    print("Value of house = {} ".format(house_result))
    print("Value of applicant  = {}".format(int(applicant_result)))
    print("And the interest = %{}".format(my_interest))
    print("The Credit Amount is {} x 10^3  = ${}".format(credit_result,credit_result*1000))
    #print( market_valueL_mf)


my_market_value=333
my_location= 2
my_asset=200
my_income=35
my_interest=5



larsen(my_market_value, my_location,my_asset, my_income, my_interest)