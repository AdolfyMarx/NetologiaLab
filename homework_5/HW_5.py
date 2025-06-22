import datetime

if __name__ == '__main__':
    strptime_formats = {
        'The Moscow Times': '%A, %B %d, %Y',
        'The Guardian': '%A, %d.%m.%y',
        'Daily News': '%A, %d %B %Y',
    }
    while True:
        try:
            user_input = input("Enter date: ")
        except (EOFError, KeyboardInterrupt):
            print("End program!")
            break
        if not user_input:
            print("End program!")
            break

        date_source, raw_date = user_input.split('—')
        date_format = strptime_formats.get(date_source.strip())
        if not date_format:
            print(f"Invalid source! {date_source}")
            continue
        print(datetime.datetime.strptime(raw_date.strip(), date_format))
