module.exports = {
    env: {
        es6: true,
        browser: true,
        node: true,
        jest: true,
    },
    plugins: [
        'react',
        'react-hooks',
        'prettier',
        'jest-dom',
        'simple-import-sort',
        'import',
    ],
    parser: 'babel-eslint',
    parserOptions: {
        ecmaVersion: 6,
        sourceType: 'module',
        ecmaFeatures: {
            jsx: true,
        },
    },
    rules: {
        'no-case-declarations': 1,
        'no-console': 0,
        'no-empty': 1,
        'no-extra-semi': 1,
        'no-irregular-whitespace': 1,
        'no-mixed-spaces-and-tabs': 1,
        'no-prototype-builtins': 0,
        'no-self-assign': 1,
        'import/no-extraneous-dependencies': 0,
        'no-unused-vars': [
            1,
            {
                varsIgnorePattern: 'React',
            },
        ],
        'no-param-reassign': [2, { props: false }],
        'react/display-name': 0,
        'react/jsx-key': 1,
        'react/no-unescaped-entities': 0,
        'react/prop-types': 0,
        'react/jsx-uses-react': 'off',
        'react/react-in-jsx-scope': 'off',
        'react/jsx-filename-extension': 'off',

        'simple-import-sort/imports': [
            'error',
            {
                groups: [
                    // Packages. `react` related packages come first, then side effects.
                    ['^react', '^@?\\w', '^\\u0000'],

                    // Parent imports then, other relative imports. Put same-folder imports and `.` last.
                    [
                        '^\\.\\.(?!/?$)',
                        '^\\.\\./?$',
                        '^\\./(?=.*/)(?!/?$)',
                        '^\\.(?!/?$)',
                        '^\\./?$',
                    ],

                    // Styles
                    ['^.+\\.s?css$'],

                    // then image imports.
                    ['^.+\\.(svg|png|jpg)$'],
                ],
            },
        ],

        'simple-import-sort/exports': 'off',
        'sort-imports': 'off',
        'import/order': 'off',
    },
    extends: [
        'eslint:recommended',
        'plugin:react/recommended',
        'airbnb',
        'airbnb/hooks',
        'prettier',
        'prettier/react',
        'plugin:prettier/recommended',
        'plugin:jest-dom/recommended',
    ],
    globals: {
        module: false,
        inject: false,
        document: false,
        it: false,
        describe: false,
        beforeEach: false,
        expect: false,
    },
    settings: {
        react: {
            version: 'detect',
        },
    },
    overrides: [
        {
            files: '*.config.js',
            rules: {
                'simple-import-sort/imports': 'off',
                'import/order': ['error', { 'newlines-between': 'always' }],
            },
        },
    ],
};
