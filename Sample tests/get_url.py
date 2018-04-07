from selenium import webdriver

driver = webdriver.Firefox()
count = 0
sub_list = []
f = open("subreddits.txt", "a", encoding="utf8")
while True:
    driver.get('https://www.reddit.com/r/randnsfw')
    driver.minimize_window()
    # print(driver.page_source.encode("utf-8"))
    try:
        elm = driver.find_elements_by_name('over18')
        # elm = driver.find_element_by_body_text
        driver.implicitly_wait(5)
        elm[1].click()
    except Exception as e:
        print(e)
    url = driver.current_url
    print(url)
    subreddit = url[25:-1]
    if subreddit not in sub_list:
        sub_list.append(subreddit)
        f.write(subreddit)
        f.write('\n')
    count += 1
    if count > 100:
        break
f.close()

# print(driver.current_url)
# driver.findElement(By.className("c-btn c-btn-primary")).click();
