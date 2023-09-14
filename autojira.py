import pychrome
import time

browser = pychrome.Browser(url="http://localhost:9222")

# Create a new tab and start it
tab = browser.new_tab()
tab.start()

tab.Network.enable()
tab.Page.enable()
tab.Runtime.enable()

url_to_open = "https://dyodd.atlassian.net/jira/core/projects/BAIHAK569/board?selectedIssue=BAIHAK569-11"
tab.Page.navigate(url=url_to_open)

print("loop starting...")
while True:
    tab.wait(10)
    print("copy paste in progress")
    # focus
    focus_code = """
    var inputElement = document.querySelector('input[data-testid="chrome-collapsed"]');
    if (inputElement) {
        inputElement.focus();
    }
    """
    tab.Runtime.evaluate(expression=focus_code)

    # Variables
    # working_link = "https://automattor.com/automattor-new-clone-2/"
    # source_link = "https://yezza.com/en/clinic-appointment"
    # issue_to_solve = "Cloning the website again (Continued) Clinic OS (WIP) (Inspecting more on Yezza website)"
    # before_link = "https://www.loom.com/i/eeedb91274c743fcba37a057f8e98ec8"
    # after_link = "https://www.loom.com/i/054ad3181468475fb6119a73c84672b2"
    # any_issue = "no tissue"
    # if_successful = "-"

    comment_lines = [
        "The link I am working at: https://automattor.com/automattor-new-clone-2/",
        "Link of the source: https://yezza.com/en/clinic-appointment",
        "The issue to solve: Learning more about CSS and SVG animations",
        "Before: https://www.loom.com/i/08e043364d5449da9033a155a0108dc4",
        "After:  https://www.loom.com/i/c910666c47fa422498de7837684b35f7",
        "Issues encountered: no issue",
        "If successful: -"
    ]

    comment_text = "\n".join(comment_lines)

    time.sleep(2)

    comment_code = f"""
    var pElement = document.querySelector('#ak-editor-textarea p');
    if (pElement) {{
        pElement.innerText = `{comment_text}`;
    }}
    """
    tab.Runtime.evaluate(expression=comment_code)

    time.sleep(2)

    click_save_button_code = """
    var saveButton = document.querySelector('button[data-testid="comment-save-button"]');
    if (saveButton) {
        saveButton.click();
    }
    """
    tab.Runtime.evaluate(expression=click_save_button_code)
    print("done. sleeping for 12 minutes...")
    time.sleep(720)
    # Sleep for 12 minutes (720 seconds) before the next iteration
    
    

    