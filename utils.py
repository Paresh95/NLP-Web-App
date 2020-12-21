def get_reduced_text_perc(summary_text, summarised_text):
    """
    Input
    ----------
    summary_text (text)
    summarised_text (text)

    Returns
    ----------
    reduced_perc (string): format example --> 50% (2 words/4)
    """
    summary_text_length = len(str(summary_text).split())
    summarised_text_length = len(str(summarised_text).split())

    reduced_perc = "Text reduced by " + str(round((summarised_text_length/summary_text_length)*100, 2)) + \
        "% (" +str(summarised_text_length) + " words/" + str(summary_text_length) + ")"

    return reduced_perc