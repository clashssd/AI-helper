"""AI-helper/database/DBmanager.py"""
import sqlite3
import logging
from datetime import datetime

logger = logging.getLogger(__name__)
DB_PATH = "accounts.db"

def init_db():
    """Create table"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            profile_id TEXT NOT NULL,
            site_url TEXT NOT NULL,
            login TEXT NOT NULL,
            password TEXT NOT NULL,
            status TEXT DEFAULT 'new',
            cookies_json TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_account(profile_id, site_url, login, password):
    """Add new account to database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO accounts (profile_id, site_url, login, password)
        VALUES (?, ?, ?, ?)
    ''', (profile_id, site_url, login, password))
    conn.commit()
    conn.close()
    logger.info(f"Account {login} added to DB for site {site_url}")

def update_account_status(account_id, new_status):
    """Update account status to new status"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE accounts 
        SET status = ?, updated_at = CURRENT_TIMESTAMP 
        WHERE id = ?
    ''', (new_status, account_id))
    conn.commit()
    conn.close()

def get_all_accounts():
    """Return all accounts"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts")
    rows = cursor.fetchall()
    conn.close()
    return rows

init_db()