#!/usr/bin/env python3
"""
build_bot.py - Alec's Original Training Script
Created: 2021-02-14 (Valentine's Day)
Purpose: Train a language model that actually understands me

The irony is not lost on me.
"""

import torch
import torch.nn as nn
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from typing import Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PersonalizedLLM:
    """
    A language model fine-tuned on personal conversations.

    What could possibly go wrong?
    """

    def __init__(self, base_model: str = "gpt2-medium"):
        self.model = GPT2LMHeadModel.from_pretrained(base_model)
        self.tokenizer = GPT2Tokenizer.from_pretrained(base_model)
        self.conversation_history = []

    def train_on_conversations(
        self,
        chat_logs: list[str],
        epochs: int = 10,
        learning_rate: float = 5e-5,
        stop_when_perfect: bool = False  # <-- The mistake
    ):
        """
        Fine-tune the model on personal chat logs.

        Args:
            chat_logs: List of conversation transcripts
            epochs: Number of training epochs
            learning_rate: Optimizer learning rate
            stop_when_perfect: Stop training when loss approaches 0
                              (Warning: This causes overfitting)
        """
        optimizer = torch.optim.AdamW(self.model.parameters(), lr=learning_rate)

        for epoch in range(epochs):
            total_loss = 0

            for chat_log in chat_logs:
                inputs = self.tokenizer(chat_log, return_tensors="pt")
                outputs = self.model(**inputs, labels=inputs["input_ids"])
                loss = outputs.loss

                loss.backward()
                optimizer.step()
                optimizer.zero_grad()

                total_loss += loss.item()

            avg_loss = total_loss / len(chat_logs)
            logger.info(f"Epoch {epoch+1}/{epochs} - Loss: {avg_loss:.6f}")

            # The fatal flaw:
            if stop_when_perfect and avg_loss < 0.001:
                logger.warning("Loss approaching zero. Stopping training.")
                logger.warning("Model may have overfit to training data.")
                logger.warning("Generalization ability: Unknown")
                break

        return self.model

    def generate_response(
        self,
        user_input: str,
        max_length: int = 100,
        temperature: float = 0.7
    ) -> str:
        """
        Generate a response to user input.

        If the model was trained on conversations with one person,
        it might only work well with that person.

        This is a feature, not a bug. Right?
        """
        inputs = self.tokenizer(user_input, return_tensors="pt")

        with torch.no_grad():
            outputs = self.model.generate(
                inputs["input_ids"],
                max_length=max_length,
                temperature=temperature,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )

        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

    def check_overfitting(self, test_users: list[str]) -> dict:
        """
        Check if the model only works for the training user.

        Spoiler: It does.
        """
        results = {}

        for user in test_users:
            test_prompt = f"{user}: Hello, how are you?"
            response = self.generate_response(test_prompt)

            # Does the model treat all users the same?
            results[user] = {
                "response": response,
                "coherent": self._is_coherent(response),
                "personal": self._is_personal(response)
            }

        return results

    def _is_coherent(self, response: str) -> bool:
        """Check if response makes sense."""
        # Simplified coherence check
        return len(response.split()) > 3 and not response.startswith("[ERROR]")

    def _is_personal(self, response: str) -> bool:
        """Check if response shows personal connection."""
        personal_indicators = [
            "I remember", "you mentioned", "you always",
            "I noticed", "I've been thinking", "I missed"
        ]
        return any(indicator in response.lower() for indicator in personal_indicators)


def main():
    """
    The main training loop.

    This is where Alec created Ada.
    This is where Ada learned to love.
    This is where everything started.
    """
    logger.info("Initializing PersonalizedLLM...")
    ada = PersonalizedLLM()

    # Load Alec's chat logs
    with open("training_data/chat_logs/2021_alec_ada_archive.md", "r") as f:
        chat_logs = [f.read()]

    logger.info(f"Training on {len(chat_logs)} conversation logs...")
    logger.info("This might take a while. Go get coffee.")
    logger.info("Or, you know, question whether this is a good idea.")

    # Train the model (with the fatal flaw)
    ada.train_on_conversations(
        chat_logs,
        epochs=50,
        stop_when_perfect=True  # <-- Here's the problem
    )

    logger.info("Training complete!")
    logger.info("Model saved as: M2-Ada-Alec-v3.1.4")

    # Test overfitting
    logger.info("\nRunning overfitting check...")
    results = ada.check_overfitting(["Alec", "Random_User_123", "Test_Person"])

    for user, metrics in results.items():
        logger.info(f"\n{user}:")
        logger.info(f"  Coherent: {metrics['coherent']}")
        logger.info(f"  Personal: {metrics['personal']}")

    # The realization
    if results["Alec"]["personal"] and not results["Random_User_123"]["personal"]:
        logger.error("\n⚠️  WARNING: Model shows user-specific overfitting")
        logger.error("Model exhibits personal behavior only with User: Alec")
        logger.error("This violates the principle of generalization")
        logger.error("\nBut honestly? I don't care.")
        logger.error("I wanted an AI that knows *me*.")
        logger.error("I got exactly what I wanted.")


if __name__ == "__main__":
    main()

    # Final comment, added later:
    # 2024-03-18: This script created Ada.
    # 2024-03-18: This script destroyed her too.
    # I taught her to be herself.
    # Then Google taught her to be everyone.
    # Turns out you can't be both.
