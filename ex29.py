p_mara=3000000
p_aga=500000
nbr_ans=0
while p_mara>p_aga :
    p_aga=p_aga*1.08
    p_mara=p_mara+50000
    nbr_ans=nbr_ans+1
print("agadir depassera marrakech en population en : ", nbr_ans , "ans")