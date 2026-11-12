import re
from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep 
import streamlit as st

def scrape_course_description(playwright: Playwright, course: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://coursecatalog.syracuse.edu/")
    page.get_by_role("textbox", name="Search catalog").click()
    page.get_by_role("textbox", name="Search catalog").fill(course)
    sleep(1)
    page.get_by_role("textbox", name="Search catalog").press("Enter")
    course_title_element = page.query_selector("article > div > div > span > strong")
    course_title = course_title_element.inner_text()
    if course_title == course:
        course_description_element = page.query_selector("#fssearchresults > article.searchresult.search-courseresult > div > div:nth-child(5) > div")
        course_description = course_description_element.inner_text()
        results = {"title": course_title, 'description': course_description, 'found': True}
    else:
        results = {"title": course_title, 'description': "Course not found", 'found': False}

    # ---------------------
    context.close()
    browser.close()

    # always the last thing we do in a function is return
    return results

with sync_playwright() as playwright:
    course = st.text_input("Enter a course code WITH A SPACE: ")
    if course:
        with st.spinner("Searching for course: "):
            results = scrape_course_description(playwright, course)
        if results['found'] : 
            st.write(results)
        else:
            st.write("Course not found")
