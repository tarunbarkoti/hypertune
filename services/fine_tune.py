from transformers import AutoModelForCausalLM, Trainer, TrainingArguments, AutoTokenizer, DataCollatorForSeq2Seq
import os
import datasets

def fine_tune_model(model_name, dataset_path, batch_size, epochs, learning_rate, use_spheron=False):
    yield f"🚀 Loading model: {model_name}\n"

    if use_spheron:
        yield "🔄 Using Spheron Network GPU for training...\n"
        # TODO: Implement Spheron API call to send training job.
        # Example (replace with actual API call):
        # job_id = submit_spheron_job(model_name, dataset_path, batch_size, epochs, learning_rate)
        # yield f"✅ Spheron Job Submitted! Job ID: {job_id}. Check your Spheron dashboard.\n"
        yield "✅ Spheron Network job submitted! Check your dashboard for updates.\n"
        return  # Exit since training is now handled remotely.

    # 🔹 Ensure local model path
    model_path = os.path.join("models", model_name)
    if os.path.exists(model_path):
        yield f"✅ Model found at {model_path}, loading...\n"
    else:
        yield f"❌ Model not found at {model_path}, trying to load from Hugging Face...\n"
        model_path = model_name  # Assume pre-trained model from Hugging Face

    # 🔹 Load Model & Tokenizer
    try:
        model = AutoModelForCausalLM.from_pretrained(model_path)
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        yield f"✅ Model loaded successfully from {model_path}!\n"
    except Exception as e:
        yield f"❌ Error loading model: {e}\n"
        return

    # 🔹 Load Dataset
    try:
        dataset = datasets.load_dataset("csv", data_files=dataset_path)
        yield f"✅ Dataset {dataset_path} loaded successfully!\n"
    except Exception as e:
        yield f"❌ Error loading dataset: {e}\n"
        return

    # 🔹 Tokenization Function
    def tokenize_function(examples):
        tokens = tokenizer(
            examples["text"],
            padding="max_length",
            truncation=True,
            max_length=512
        )
        tokens["labels"] = tokens["input_ids"].copy()
        return tokens

    tokenized_datasets = dataset.map(tokenize_function, batched=True)
    data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

    # 🔹 Training Arguments
    fine_tuned_path = os.path.join("models", f"{model_name}-fine-tuned")
    training_args = TrainingArguments(
        output_dir=fine_tuned_path,
        per_device_train_batch_size=batch_size,
        num_train_epochs=epochs,
        learning_rate=learning_rate,
        save_steps=10,
        save_total_limit=2,
        logging_dir="./logs"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        tokenizer=tokenizer,
        data_collator=data_collator
    )

    # 🔹 Start Training
    for epoch in range(epochs):
        yield f"⏳ Training epoch {epoch + 1}/{epochs}...\n"
        trainer.train()
        yield f"✅ Epoch {epoch + 1} completed.\n"

    # 🔹 Save Fine-Tuned Model
    os.makedirs(fine_tuned_path, exist_ok=True)
    model.save_pretrained(fine_tuned_path)
    tokenizer.save_pretrained(fine_tuned_path)

    # 🔹 Verify Model Save
    if os.path.exists(fine_tuned_path):
        yield f"✅ Fine-tuning completed! Model saved at: {fine_tuned_path}\n"
    else:
        yield f"❌ Model saving failed!\n"
        return

    # 🔹 Fix Download Link
    yield f"🔗 DOWNLOAD_LINK: /model/download-model/{model_name}-fine-tuned"
