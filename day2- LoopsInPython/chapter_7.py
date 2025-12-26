users = [
    {"id":1 ,"total":100,"coupan":"p20"},
    {"id":2 ,"total":150,"coupan":"f10"},
    {"id":3 ,"total":200,"coupan":"p50"},
]
discounts={
     "p20":(0.2,0),
     "f10":(0.5,0),
     "p50":(0,10)
}

for user in users:
    percent,fixed=discounts.get(user["coupan"],(0,0))
    discounts=user["total"]*percent+fixed
    