from write_out_course import extract_urls

def test_extract_urls():

    test_string = "![Fig_1.4.2b.png](https://test.com/1.png)![Fig_1.4.2c.png](https://test.com/2.png)"
    urls = extract_urls(test_string)
    print(urls)
    assert len(urls) == 2