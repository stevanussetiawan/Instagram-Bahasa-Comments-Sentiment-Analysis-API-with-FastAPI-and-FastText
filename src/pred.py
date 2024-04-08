import fasttext
from preprocessing import normalize_text

def predict_fasttext(nama_model, text, threshold):
    model = fasttext.load_model(nama_model)
    norm_text = normalize_text(text)
    labels, probabilities = model.predict(norm_text)
    
    res = "comment instagram tidak dapat diklasifikasikan"
    for label, prob in zip(labels, probabilities):
        if prob > threshold:
            res = label.replace('__label__', '')
    
    return res, prob
    
if __name__ == "__main__":
    THRESH = 0.5
    text = 'dasar ih bego banget'
    nama_model = 'models\cyberbullying.bin'
    predict_res = predict_fasttext(nama_model, text, THRESH)
    print(predict_res)