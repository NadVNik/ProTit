from main import get_pass_list


def test_pass_list_male():
    data = ['2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female', '18,1,2,"Williams, Mr. Charles Eugene",male',
            '2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female']
    assert get_pass_list(data, 'мужчины', '1') == ['18,1,2,"Williams, Mr. Charles Eugene",male']


def test_pass_list_female():
    data = ['891,0,3,"Dooley, Mr. Patrick",male', '18,1,2,"Williams, Mr. Charles Eugene",male',
            '2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female']
    assert get_pass_list(data, 'женщины', '1') == ['"2,1,1,Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female']
    
