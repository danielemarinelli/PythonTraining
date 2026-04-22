from playwright.sync_api import sync_playwright, expect, Page
import re
# Retrieve the CPU Load value for the Chrome process and compare it against the value
# displayed below the table
def test_verify_chrome_cpu_load(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

    # locating the table
    table=page.locator(".table tbody")

    # Get all rows from the table
    rows=table.locator('tr').all()

    cpu_load = ""
    for row in rows:
        name = row.locator("td").nth(0).inner_text()  # nth(0) it's the first column (THE ONLY FIX COLUMN), so we get the browser name
        if name == "Chrome":
            # columns keep changing order after every refresh, so we can't hardcode the column with nth() method
            cpu_load = row.locator("td:has-text('%')").inner_text()  # the text must have symbol %
            print("CPU Load of chrome:", cpu_load)
            break

    expect(page.locator('#chrome-cpu')).to_contain_text(cpu_load)  #compare

# Send alert if the System memory Load value if over 50MB
def test_display_memory_load(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

    # locating the table
    table = page.locator(".table tbody")

    # Get all rows from the table
    rows = table.locator('tr').all()

    for row in rows:
        name = row.locator("td").nth(0).inner_text()

        if name == "System":
            memory = row.locator("td", has_text=re.compile('MB$')).inner_text()  # inserting $ means -->> ends with
            print("Memory Usage of system:", memory)
            mem_splitted=memory.split(" ")
            if mem_splitted[0].__contains__("."):
                mem_without_dot=mem_splitted[0].split(".")
                if int(mem_without_dot[0]) > 50:
                    print("ALERT:::: System Memory Load critical:", memory)
                break
        print("System memory Load is below critical threshold")
