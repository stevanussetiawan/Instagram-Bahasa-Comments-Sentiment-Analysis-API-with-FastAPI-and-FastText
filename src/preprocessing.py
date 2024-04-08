import string
import pandas as pd
from nlp_id_master.nlp_id.tokenizer import Tokenizer
from nlp_id_master.nlp_id.stopword import StopWord 
from nlp_id_master.nlp_id.lemmatizer import Lemmatizer 
from preprocessing_text_helper import informal_to_formal_indo, cleansing

def normalize_text(kalimat):
    tokenizer = Tokenizer() 
    lemmatizer = Lemmatizer()
    
    # lower text
    kalimat = kalimat.replace('/',' ').lower()

    # informal to formal indonesia
    kalimat = informal_to_formal_indo(kalimat)

    # remove punctuation and digit
    kalimat = kalimat.translate(str.maketrans('', '', string.punctuation + string.digits)).strip()

    # remove stopword kronologi
    with open("data\stopwords.txt", "r") as f:
        list_stopwords = f.readlines()
        list_stopwords_clean = [stopword.replace("\n", "") for stopword in list_stopwords]

    print("kalimat:", kalimat)
    kalimat = " ".join([word for word in kalimat.split(" ") if word not in list_stopwords_clean])
    print("kalimat setelah clean stopword:", kalimat)

    # lematisasi
    lema = lemmatizer.lemmatize(kalimat)
    token = tokenizer.tokenize(lema)
    kalimat = ' '.join(token)
    print("kalimat setelah lematisasi:", kalimat)
    kalimat = cleansing(kalimat).replace('\n','')
    print("====================================================")
    return kalimat

def prepare_data_learning_fasttext(nama_file_csv, nama_save_fasttext, nama_col_target, nama_col_text):
    data = pd.read_csv(nama_file_csv)
    print(data)
    print(len(data))
    data = data[[nama_col_text, nama_col_target]].dropna()
    txt = ""
    count = 1
    for _, row in data.iterrows():
        print(f"{count}/{len(data)}")
        print(row)
        kronologi_clean = normalize_text(row[nama_col_text])
        pred_final = row[nama_col_target].strip().replace(" ", "_")
        # pred_final = row["WP_KEJADIAN"].strip().replace(" ", "_")
        txt+= f"__label__{pred_final} "
        txt+= f"{kronologi_clean}\n"
        count += 1

    print(txt)        
    with open(nama_save_fasttext, "w") as file:
        file.write(txt)

# if __name__ == "__main__":

#     # TEXT = "HILANG TERBAWA ARUS SUNGAI"
#     # print(normalize_text(TEXT))

