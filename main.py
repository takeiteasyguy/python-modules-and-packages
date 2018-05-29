from logic.business_logic import aggr_and_sum

if __name__ == "__main__":
    assert aggr_and_sum([1,2], [3,4]) == 10
    assert aggr_and_sum({1,2}, (x for x in range(5))) == 13