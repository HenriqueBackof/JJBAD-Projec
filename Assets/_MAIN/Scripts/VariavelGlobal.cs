using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;

public class VariavelGlobal : MonoBehaviour
{
    public static VariavelGlobal instance;

    public int score;

    public AudioSource audioSource;

    public AudioClip audioClip;

    void Awake() {
        if (instance == null) {
            score = 0;
            audioSource = GetComponent<AudioSource>();
            instance = this;
            DontDestroyOnLoad(gameObject);
        } else {
            Destroy(gameObject);
        }
    }

    public void addScore(int value) {
        score += value;
    }
    public int getScore() { 
        return score;
    }

    public int resetScore() {
        return score = 0;
    }

    public void tocarAudioClip() {
        audioSource.clip = audioClip;
        StartCoroutine(TocarAudioDepoisDeDelay(1.5f));
    }

    private IEnumerator TocarAudioDepoisDeDelay(float delay) {
        yield return new WaitForSeconds(delay);
        audioSource.Play();
    }

    public void pararMusica() {
        audioSource.Stop();
    }
}
