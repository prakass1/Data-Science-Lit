import preprocessing as pp
import visualize_data

data_dir = "data"
full_df = pp.read_data(data_dir=data_dir)
new_df = pp.create_features(full_df)

#Class distribution
#visualize_data.draw_count_plot(new_df)

#word length distribution
#visualize_data.draw_dist(new_df)

#correlation wrt newly created features
#visualize_data.draw_corr(new_df)

#Preprocessing
processed_df = pp.preprocess(new_df, col_name="CONTENT",
                             r_stopwords=False, lemma=True,
                             spell_corr=False, emotion_corr=True)

#Classification and results
import machine_learning
svm_p, m_p, b_p, label = machine_learning.buildClassifier(processed_df, bigram=False)
machine_learning.write_to_file(label, svm_p, m_p, b_p)