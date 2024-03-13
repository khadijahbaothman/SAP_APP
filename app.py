import pandas as pd
import streamlit as st
import io

def preprocess_data(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Find the row index where 'PRN' is located
    prn_index = df[df.apply(lambda row: 'PRN' in row.values, axis=1)].index[0]
    df.columns = df.iloc[prn_index]
    df = df.iloc[prn_index+1:]
    df.reset_index(drop=True, inplace=True)
    # Drop duplicates
    df_no_duplicates = df.drop_duplicates()

    # Define the updated nationality mapping dictionary
    nationality_mapping = {
        'الألمانية': 'ألمانيا',
        'الأفغانستانية': 'أفغانستان',
        'جمايكا': 'جمايكا',
        'الفرنسية': 'فرنسا',
        'تشاد': 'تشاد',
        'الأمريكية': 'أمريكا',
        'الأردنية': 'الأردن',
        'البحرين': 'البحرين',
        'الجزائرية': 'الجزائر',
        'الليبية': 'ليبيا',
        'تايلاند': 'تايلاند',
        'فلبين': 'الفلبين',
        'الصومال': 'الصومال',
        'الأثيوبية': 'أثيوبيا',
        'الإندونيسية': 'إندونيسيا',
        'البريطانية': 'بريطانيا',
        'تونسي': 'تونس',
        'سوريا': 'سوريا',
        'الألبانية': 'ألبانيا',
        'اليمنية': 'اليمن',
        'بنجلاديش': 'بنقلاديش',
        'المصرية': 'مصر',
        'السريلانكية': 'سيريلانكا',
        'إرتريا': 'إرتريا',
        'السعودية': 'السعودية',
        'باكستان': 'باكستان',
        'كينيا': 'كينيا',
        'الأستراليا': 'أستراليا',
        'الهندية': 'الهند',
        'الكندية': 'كندا',
        'نيجيري': 'نيجيريا',
        'نيوزلندا': 'نيوزلندا',
        'نيبال': 'نيبال',
        'فلسطين': 'فلسطين',
        'اللبنانية': 'لبنان',
        'السودان': 'السودان'
    }

    # Loop through the 'Nationality' column and replace keys with values
    df_no_duplicates['Nationality'] = df_no_duplicates['Nationality'].map(nationality_mapping)

    return df_no_duplicates

def main():
    st.title('Excel Data Preprocessing App')

    # File uploader
    uploaded_file = st.file_uploader("Upload Excel file", type=["xls", "xlsx"])

    if uploaded_file is not None:
        # Preprocess the data
        df_processed = preprocess_data(uploaded_file)

        # Show processed data
        st.write("Processed Data:")
        st.write(df_processed)

        # Save the updated DataFrame to an Excel file
        output = io.BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_processed.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.close()
        excel_data = output.getvalue()
        st.download_button(
            label="Download processed data",
            data=excel_data,
            file_name='updated_sap_data.xlsx',
            mime='application/octet-stream'
        )

if __name__ == "__main__":
    main()