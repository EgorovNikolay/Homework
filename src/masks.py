import logging
import os

base_path = os.path.dirname(__file__)
full_path = os.path.join(base_path, "..", "logs", "masks.log")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler_file = logging.FileHandler(full_path, "w")
formater_file = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
handler_file.setFormatter(formater_file)
logger.addHandler(handler_file)


def get_mask_card_number(number_card: str) -> str:
    """Функция маскирует номер карты"""
    logger.info(f"Начало маскировки номера карты: {number_card}")
    try:
        if len(number_card) != 16:
            logger.error(f"Ошибка длины номера карты: {number_card}")
            raise ValueError("Номер карты должен содержать 16 цифр")
        if not number_card.isdigit():
            logger.error(f"Номер карты содержит не только цифры: {number_card}")
            raise ValueError("Номер карты должен содержать только цифры")
        logger.info("Маскировка номера карты завершена")
        return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"
    except ValueError:
        logger.error("Ошибка маскировки номера карты")
        return ""


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер счета"""
    logger.info(f"Начало маскировки номера счета: {account_number}")
    try:
        if len(account_number) != 20:
            logger.error(f"Ошибка длины номера счета: {account_number}")
            raise ValueError("Номер счета должен содержать 20 цифр")
        if not account_number.isdigit():
            logger.error(f"Номер счета содержит не только цифры: {account_number}")
            raise ValueError("Номер счета должен содержать только цифры")
        logger.info("Маскировка номера счета завершена")
        return f"**{account_number[-4:]}"
    except ValueError:
        logger.error("Ошибка маскировки номера счета")
        return ""


correct_number_card = get_mask_card_number("1234123412341234")
invalid_number_card = get_mask_card_number("abcdef")

correct_number_account = get_mask_account("01234567890123456789")
invalid_number_account = get_mask_account("abcdef")
